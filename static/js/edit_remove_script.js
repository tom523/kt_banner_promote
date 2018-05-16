// $('#edit').click(function () {
//     content_html = '    <div class="king-block-content">\n' +
//         '        <form class="form-horizontal" method="POST">\n' +
//         '            <div class="form-group">\n' +
//         '                <label for="inputCount3" class="col-sm-3 control-label">帐号：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <input type="text" class="form-control" id="inputCount3" placeholder="用户名/QQ号码/手机号码">\n' +
//         '                </div>\n' +
//         '                <span class="text-danger mt5 fl">*</span>\n' +
//         '            </div>\n' +
//         '            <div class="form-group">\n' +
//         '                <label for="inputEmail3" class="col-sm-3 control-label">邮箱：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <input type="email" class="form-control" id="inputEmail3" placeholder="输入邮箱帐号">\n' +
//         '\n' +
//         '                </div>\n' +
//         '                <span class="text-danger mt5 fl">*</span>\n' +
//         '            </div>\n' +
//         '            <div class="form-group">\n' +
//         '                <label for="inputPassword3" class="col-sm-3 control-label">密码：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <input type="password" class="form-control" id="inputPassword3" placeholder="">\n' +
//         '                    <p class="help-block">6位以上，仅可由数字、字母、下划线组成</p>\n' +
//         '                </div>\n' +
//         '                <span class="text-danger mt5 fl">*</span>\n' +
//         '            </div>\n' +
//         '            <div class="form-group">\n' +
//         '                <label for="inputEmail3" class="col-sm-3 control-label">地区：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <select name="" id="" class="form-control">\n' +
//         '                        <option value="深圳">深圳</option>\n' +
//         '                        <option value="北京">北京</option>\n' +
//         '                        <option value="上海">上海</option>\n' +
//         '                        <option value="广州">广州</option>\n' +
//         '                    </select>\n' +
//         '                </div>\n' +
//         '            </div>\n' +
//         '            <div class="form-group">\n' +
//         '                <label class="control-label col-sm-3">兴趣爱好：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <div class="checkbox">\n' +
//         '                        <label class="mr10">\n' +
//         '                            <input type="checkbox" value="">运动\n' +
//         '                        </label>\n' +
//         '                        <label class="mr10">\n' +
//         '                            <input type="checkbox" value="">音乐\n' +
//         '                        </label>\n' +
//         '                        <label>\n' +
//         '                            <input type="checkbox" value="" disabled="">上网（禁用）\n' +
//         '                        </label>\n' +
//         '                    </div>\n' +
//         '                </div>\n' +
//         '            </div>\n' +
//         '            <div class="form-group">\n' +
//         '                <label class="control-label col-sm-3">性别：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <div class="radio">\n' +
//         '                        <label class="mr10">\n' +
//         '                            <input type="radio" name="optionsRadios" id="optionsRadios1" value="" checked="">男\n' +
//         '                        </label>\n' +
//         '                        <label>\n' +
//         '                            <input type="radio" name="optionsRadios" id="optionsRadios2" value="">女\n' +
//         '                        </label>\n' +
//         '                    </div>\n' +
//         '                </div>\n' +
//         '            </div>\n' +
//         '            <div class="form-group has-feedback">\n' +
//         '                <label class="control-label col-sm-3" for="introduction">个人说明：</label>\n' +
//         '                <div class="col-sm-7">\n' +
//         '                    <textarea class="form-control" rows="3" id="introduction"></textarea>\n' +
//         '                </div>\n' +
//         '            </div>\n' +
//         '            <div class="form-group">\n' +
//         '                <div class="col-sm-7 col-sm-offset-3">\n' +
//         '                    <input type="button" class="king-btn king-success mr10" value="提交">\n' +
//         '                    <input type="reset" class="king-btn king-default" value="取消">\n' +
//         '                </div>\n' +
//         '            </div>\n' +
//         '        </form>\n' +
//         '    </div>'
//     var d = dialog({
//         width: 600,
//         title: 'message',
//         content: content_html,
//         okValue: "确定",
//         ok: function () {
//         },
//         cancelValue: '取消',
//         cancel: function () {
//         },
//     });
//     d.showModal();
// });

//活动延期

// $("a[data-id]").click(function () {
//     alert(this)
// })
// function change_store(banner_id) {
//     alert(banner_id)
// }

function errorAlert(message) {
    var d = dialog({
        width: 260,
        title: '提示',
        cancel: function (){},
        ok: function() {},
        okValue: '确定',
        content: '<div class="king-notice-box king-notice-fail"><p class="king-notice-text">'+message+'</p></div>',
        cancelValue: '取消',
        cancel: function() {
            // do something
        }
    });
    d.show();
}

function successAlert(message) {
    var d = dialog({
        width: 260,
        title: '提示',
        cancel: function (){},
        ok: function() {},
        okValue: '确定',
        content: '<div class="king-notice-box king-notice-success"><p class="king-notice-text">'+message+'</p></div>',
        cancelValue: '取消',
        cancel: function() {
            // do something
        }
    });
    d.show();

}

function expand(banner_id) {
    content_html = '                    <div class="input-group date" id="plugin9_demo2" data-date="" data-date-format="dd MM yyyy" data-link-field="dtp_input2" data-link-format="yyyy-mm-dd">\n' +
        '                        <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>\n' +
        '                        <input class="form-control" id="new_expandto" size="6" type="text" value="">\n' +
        '                        <input type="hidden" id="dtp_input2" value="">\n' +
        '                        <br>\n' +
        '                    </div>\n' +
        '                    <script type="text/javascript">\n' +
        '                        //日期选择器(Bootstrap)-2，日期选择\n' +
        '                        $(\'#plugin9_demo2\').datetimepicker({\n' +
        '                            language:  \'zh-TW\',\n' +
        '                            weekStart: 1,\n' +
        '                            todayBtn:  true,\n' +
        '                            autoclose: true,\n' +
        '                            todayHighlight: true,\n' +
        '                            startView: 2,\n' +
        '                            minView: 2,\n' +
        '                            forceParse: false,\n' +
        '                            format:"yyyy-mm-dd",\n' +
        '                        });\n' +
        '                    </script>'
    var d = dialog({
        width: 300,
        title: '延期天数【'+banner_id+'】',
        content: content_html,
        okValue: "确定",
        ok: function () {
            new_expandto = $('#new_expandto').val()
            url = 'promote_expand?new_expandto='+ new_expandto + '&banner_id=' + banner_id
            $('#loding-img-2').show()
            $.get(url, function (result) {
                $('#expand' + banner_id).text(new_expandto + " 00:00:00")
                successAlert("延期成功")
                $('#loding-img-2').hide()
            }, 'json')
        },
        cancelValue: '取消',
        cancel: function () {
        },
    });
    d.showModal();
}

function change_store(banner_id) {
    console.log("执行修改餐厅操作：change_store")
    $('#upload_storeid').addClass('hidden')
    $('#forbidden_layer').show()
    $('#loding-img-2').show()
    //获取门店信息
    store_query_url = 'except_store_query'

    xhttrequest = $.get(store_query_url, {banner_id:banner_id}, function (retdata) {
        $('#loding-img-2').hide()
        console.log(retdata.message)
        $('#forbidden_layer').hide()
         // for(var i=0; i<retdata.message.length;i++){
         //     retdata.message[i].checked = true
         // }
        var treeview = $('#listenersDemoTree').data('kendoTreeView');
        treeview.setDataSource(new kendo.data.HierarchicalDataSource({
            'data': retdata.message
        }));
        listenerDemo._onCheck()
        $('#upload_storeid').removeClass('hidden')

        // 确认提交更改
        $('#upload_storeid').click(function (){
            $('#loding-img-2').show()
            $('#forbidden_layer').show()
            except_store_id_post_url = 'except_store_id_post'
            storedata = listenerDemo.selected
            console.log("确认提交except_store_id:" + storedata)
            postdata = {
                join_store: JSON.stringify(storedata),
                banner_id: banner_id,
            }
            console.log(postdata)
            $.ajax({
              url: except_store_id_post_url,
              type: "POST",
               data: postdata,
              dataType: 'json',
               headers: {"X-CSRFtoken":$.cookie("csrftoken")},
              success: function (retdata) {
                  if(retdata.result == "success")
                  {
                      console.log(retdata)
                      $('#forbidden_layer').hide()
                      $('#loding-img-2').hide()
                      var d = dialog({
                        width: 260,
                        title: '提示',
                        cancel: function (){},
                        ok: function() {},
                        okValue: '确定',
                        content: '<div class="king-notice-box king-notice-success"><p class="king-notice-text">添加记录成功！</p></div>',
                        cancelValue: '取消',
                        cancel: function() {
                            // do something
                        }
                      });
                      d.show();
                  }
              },
              error: function (retdata) {
                  alert("更新异常，联系开发者！！！")
              }
            })


        });

    }, 'json')
    // $('#upload_storeid').click(function () {
    //     $('#forbidden_layer').addClass('hidden')
    //     xhttrequest.abort()
    //     $('#loding-img-2').hide()
    // });

    $('#side_content_cancel').click(function () {
        console.log($('#inner_query_btn'));
        $('#forbidden_layer').addClass('hidden')
        xhttrequest.abort()
        $('#loding-img-2').hide()
    });
}

//待查询的门店ID必须是多个6位数字，且以英文逗号分隔的字符串
function isArrayItemNo(str) {
    for(var i=0; i<str.length; i++){
        if(isNo(str[i])){
            continue;
        }else{
            return false
        }
    }
    return true;
}
function isNo(str) {
    var reg=/^[0-9]{6}$/;
    return reg.test(str);
}


function query_store_id(bannerid) {
    console.log("开始执行【ID查询】" + bannerid)
    console.log($('#forbidden_layer'))
    $('#side_content_query_id_title').text(bannerid)
    $('#forbidden_layer').show()
    //清空之前查询的结果
    $('#query_result_not_in').text('')
    $('#query_result_in').text('')
    $('#storeid_textarea').val('')
    $('#query_result_not_in_wrap').hide()
    $('#query_result_in_wrap').hide()
    //清除之前点击时的绑定事件，重新绑定。
    $('#inner_query_btn').unbind();
    $('#inner_query_btn').click(function () {
        //检查输入是否合法
        //正常输入：101877,102004,102323,102451,100016,102073,101275
        storeids = $('#storeid_textarea').val()
        console.log(storeids)
        idArray = storeids.split(',')
        if(storeids == ""){
            errorAlert("查询门店ID不能为空")
        }else if(!isArrayItemNo(idArray)){
            errorAlert("非正常门店ID，门店ID必须是1个或多个6位数字，并且以英文逗号分隔。")
        }
        else{
            //    提交数据给后端
            $('#loding-img-2').show()
            $('#forbidden_layer').show()
            postdata = {
                queryids: storeids.trim(),
                bannerid: bannerid,
            }
            submit_query_storeid_url = 'submit_query_storeid_url'
            $.ajax({
              url: submit_query_storeid_url,
              type: "POST",
               data: postdata,
              dataType: 'json',
               headers: {"X-CSRFtoken":$.cookie("csrftoken")},
              success: function (retdata) {
                  $('#query_result_not_in_wrap').show()
                  $('#query_result_in_wrap').show()
                  $('#loding-img-2').hide()
                  if(retdata.result == "success")
                  {
                      console.log(retdata.data)
                      textstr_not_in = ""
                      item_obj_not_in = retdata.data.not_in_exceptStore_obj_dict
                      for(var key in item_obj_not_in){
                          textstr_not_in += "<span style='display: inline-block; width: 150px;'>"
                              + item_obj_not_in[key] + "(" + key + ")" + "</span>"
                      }
                      $('#query_result_not_in').html(textstr_not_in)
                      textstr_in = ""
                      item_obj_in = retdata.data.in_exceptStore_obj_dict
                      for(var key in item_obj_in){
                          textstr_in += "<span style='display: inline-block; width: 150px;'>"
                              + item_obj_in[key] + "(" + key + ")" + "</span>"
                      }
                      $('#query_result_in').html(textstr_in)
                      
                  //    将不在exceptStore字段的id添回到exceptStore字段
                      var ids_array = new Array()
                      var i = 0
                      for(var key in item_obj_not_in){
                          ids_array[i]=key;
                          i++
                      }
                      //清除上次提交时的绑定事件，重新绑定。
                      //关闭门店活动
                      $('#submitTo_exceptStore').unbind()
                      $('#submitTo_exceptStore').click(function () {
                          $('#loding-img-2').show()
                          var postdata = {
                              bannerid: bannerid,
                              ids:ids_array.join(','),
                          }
                          url = 'addTo_exceptStore'
                          $.ajax({
                              url: url,
                              type: "POST",
                              data: postdata,
                              dataType: 'json',
                              headers: {"X-CSRFtoken":$.cookie("csrftoken")},
                              success: function (retdata) {
                                  $('#loding-img-2').hide()
                                  console.log("关闭门店活动成功：" + postdata.ids)
                                  console.log(retdata)
                                  if(retdata.result = "success"){
                                      successAlert("关闭门店成功")
                                      location.href = '#side_content_query_id_close'
                                      $('#forbidden_layer').hide()
                                  }
                              }
                          })
                      })

                      //开启门店活动
                      var ids_array_in = new Array()
                      var j = 0
                      for(var key in item_obj_in){
                          ids_array_in[j]=key;
                          j++
                      }

                      $('#removeFrom_exceptStore').unbind()
                      $('#removeFrom_exceptStore').click(function () {
                          $('#loding-img-2').show()
                          var postdata = {
                              bannerid: bannerid,
                              ids:ids_array_in.join(','),
                          }
                          console.log(postdata)
                          url = 'removeFrom_exceptStore'
                          $.ajax({
                              url: url,
                              type: "POST",
                              data: postdata,
                              dataType: 'json',
                              headers: {"X-CSRFtoken":$.cookie("csrftoken")},
                              success: function (retdata) {
                                  $('#loding-img-2').hide()
                                  console.log("开启门店活动成功：" + postdata.ids)
                                  console.log(retdata)
                                  if(retdata.result = "success"){
                                      successAlert("开启成功")
                                      location.href = '#side_content_query_id_close'
                                      $('#forbidden_layer').hide()
                                  }
                              }
                          })
                      })

                  }
              },
              error: function (retdata) {
                  errorAlert(retdata)
              }
          })

        }

    })
    console.log($('#side_content_cancel'))
    $('#queryid_side_content_cancel').click(function () {
        console.log($('#inner_query_btn'));
        $('#forbidden_layer').hide()
        $('#loding-img-2').hide()
    });
}


function do_exceptStore(bannerid){
    content_html = "    <div class=\"king-page-box\">\n" +
        "        <div class=\"king-container clearfix\">\n" +
        "            <form class=\"form-horizontal\">\n" +
        "                <div class=\"form-group has-feedback clearfix \">\n" +
        "                    <label class=\"control-label col-sm-3 pt0\" for=\"introduction\">门店ID：</label>\n" +
        "                    <div class=\"col-sm-9\">\n" +
        "                        <textarea id=\"store_ids\" class=\"form-control\" rows=\"6\" placeholder=\"填入以逗号分隔的6位数字\"></textarea>\n" +
        "                    </div>\n" +
        "                </div>\n" +
        "            </form>\n" +
        "        </div>\n" +
        "    </div>"
    var d = dialog({
        width: 600,
        title: '门店活动到期【'+bannerid+'】',
        content: content_html,
        okValue: "确定",
        ok: function () {
            store_id_array = $('#store_ids').val().split(',')
            $.get(site_url + 'add_storeid_to_exceptStore', {data: store_id_array, banner_id: bannerid}, function (res) {
                if(res.result){
                    successAlert("添加门店ID成功")
                }else{
                    errorAlert("failed")
                }
            })
        },
        cancelValue: '取消',
        cancel: function () {
        },
    });
    d.showModal();
}





