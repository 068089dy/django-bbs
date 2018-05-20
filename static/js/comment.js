
title = $('div.card>div.container>div.card-content>h4');
    //alert(title)
    title_btn = $('div.card>div.container>div.card-content>a.btn-flat');
    c(title_btn.eq(2));
    c(title_btn.eq(3));
    thump_btn = $('div.card>a.btn-flat');
    for(var i = 0; i<thump_btn.length;i++){
        c(thump_btn.eq(i));
    }
    function c(btn){
        btn.click(function(){
            $.ajax({
                url: '/ajax_test/',
                type: 'get',
                success: function(data) {
                    btn.html("<i class=\"material-icons left\">thumb_up</i>"+data)
                },
                failure: function(data) { 
                    alert('Got an error dude');
                }
            }); 
        })
    }
    
    
    