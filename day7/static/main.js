$(document).ready(function(){
    $(document).on('click', '#id_list tr', function(){
        fn_search($(this).find('td').eq(2).text());
        });
        function fn_search(param){
            $.ajax({
                url : 'http://localhost:5555/main'
                ,dataType : 'json'
                ,type : 'POST'
                ,data : JSON.stringify({'test':param})
                ,success : function(data){
                console.log(data);
                },error(e){
                console.log(e);
                }
            });
       }
});