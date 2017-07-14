/**
 * Created by lekanterragon on 7/12/17.
 */


var handleAjaxRoute = function (apiURI, payload) {
                      $.ajax({
                              url : apiURI,
                              type:  "GET",
                              data : JSON.stringify(payload),
                              contentType: 'application/json',
                              dataType:"json",
                              success : function (response) {
                          },
                              error : function(xhr, errmsg, err){

                                }
                            })
};