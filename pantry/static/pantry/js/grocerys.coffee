log = -> console.log.apply console, arguments

log 'why hello there (from coffeescript).'

# request = $.ajax
#   url: '/API-REST-1/grocerys/'
#   type: 'GET'
#   data: {}
#   # accepts: 'json' # results in 406 unacceptable from django api server
#   success: (data, err_str, jqXHR) -> log "success '#{err_str}'", data
#   error: (jqXHR, err_str, exception) -> log "error '#{err_str}'", exception
#   complete: (jqXHR, err_str) -> log "complete '#{err_str}'"

class Model
  @get_all = (success) ->
    $.ajax
      url: @_url
      type: 'GET'
      data: {}
      # accepts: 'json' # results in 406 unacceptable from django api server
      success: (data, err_str, jqXHR) ->
        unless success? then log "success '#{err_str}'", data
        success? data
      error: (jqXHR, err_str, exception) -> log "error '#{err_str}'", exception
      complete: (jqXHR, err_str) -> log "complete '#{err_str}'"


class GroceryModel extends Model
  @_url = '/API-REST-1/grocerys/'

class RecipeModel extends Model
  @_url = '/API-REST-1/recipes/'


_.templateSettings = interpolate : /\{\{(.+?)\}\}/g



$ =>
  GroceryModel.get_all (groceries) ->
    for grocery in groceries
      template = _.template "<div> grocery: {{ name }} </div>"
      html = template grocery
      log grocery
      $('.grocerylist').append html

  RecipeModel.get_all (recipes) ->
    for recipe in recipes
      template = _.template "<div> recipe: {{ name }} </div>"
      html = template recipe
      log recipe
      $('.recipelist').append html
