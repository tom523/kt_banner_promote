$(function(){

    function renderTpl(str, cfg) {
        var re = /(#(.+?)#)/g;

        return str.replace(re, function() {
            var val = cfg[arguments[2]]+'';
            if(typeof val == 'undefined') {
                val = '';
            }
            return val;
        });
    }

    $('#loding-img-2').show()
    $('#forbidden_layer').show()
    console.log($('#forbidden_layer'))
    // 异步请求后台数据
    $.ajax({
        url: 't_bi_banner',
        type: 'GET',
        success: function(res){
            $('#loding-img-2').hide()
            $('#forbidden_layer').hide()
            var _html = ' ';
            var list = res.items;
            var tpl = $('#tpl_15233690356952').html();
            var headerTpl =  $('#header_tpl_15233690356952').html();
            for (var i=0,len=list.length; i < len; i++){
                var item = list[i];
                _html += renderTpl(tpl, item)
            }
            $('.ranger-box2 tbody').html(_html);
            $('.ranger-box2 thead').html(renderTpl(headerTpl,res.catalogues));
        }
    });
    
});


