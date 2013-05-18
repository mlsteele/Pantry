log = -> console.log.apply console, arguments

log 'why hello there (from coffeescript).'

increment_count = (obj) ->
  obj.count += 1

  $.ajax
    url: obj.url
    type: 'PUT'
    data: obj
    # accepts: 'json' # results in 406 unacceptable from django api server
    success: (data, err_str, jqXHR) -> log "success '#{err_str}'", data
    error: (jqXHR, err_str, exception) ->
      log "error '#{err_str}'"
      log "exception", exception
    complete: (jqXHR, err_str) -> log "complete '#{err_str}'"

request = $.ajax
  url: '/API-REST-1/grocerys/'
  type: 'GET'
  data: {}
  # accepts: 'json' # results in 406 unacceptable from django api server
  success: (data, err_str, jqXHR) ->
    log "success '#{err_str}'", data
    log increment_count data
  error: (jqXHR, err_str, exception) -> log "error '#{err_str}'"
  complete: (jqXHR, err_str) -> log "complete '#{err_str}'"

log request
