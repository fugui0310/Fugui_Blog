 $("#avatar_file").change(function () {

        var ele_file=$(this)[0].files[0];  //this.files
        var reader=new FileReader();
        reader.readAsDataURL(ele_file);
        reader.onload=function () {
            $("#avatar_img")[0].src=this.result
        }

    });

    $("#subBtn").click(function () {

        var formdata=new FormData();
        formdata.append("username",$("#id_username").val());
        formdata.append("password",$("#id_password").val());
        formdata.append("repeat_password",$("#id_repeat_password").val());
        formdata.append("email",$("#id_email").val());
        formdata.append("avatar_img",$("#avatar_file")[0].files[0]);

        $.ajax({
            url:"/reg/",
            type:'POST',
            data:formdata,
            contentType:false,
            processData:false,
            headers:{"X-CSRFToken":$.cookie('csrftoken')},
            success:function (data) {
                  console.log(data);
                var data =JSON.parse(data);

                if (data.user){
                    location.href="/login/"
                }
                else {

                    console.log(data.errorsList);

                   $.each(data.errorsList,function (i,j) {
                       console.log(i,j);

                       $span=$("<span>");
                       $span.addClass("pull-right").css("color","red");
                       $span.html(j[0]);
                       $("#id_"+i).after($span).parent().addClass("has-error")

                       if (i=="__all__"){
                            $("#id_repeat_password").after($span)
                       }
                   })


                }


            }
        })
    })