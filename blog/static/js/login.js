


$("#subbtn").click(function () {
        $.ajax({
            url: "/login/",
            type: "POST",
            data: {
                "username": $("#username").val(),
                "password": $("#password").val(),
                "validCode": $("#validCode").val(),
                "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val(),
            },
            success: function (data) {
                console.log(data);

                var response = JSON.parse(data);
                if (response["is_login"]) {
                    location.href = "/index/"
                }
                else {
                    $(".error").html(response["error_msg"]).css("color", "red")
                }
            }
        })
    });
    $(".validCode_img").click(function () {
        $(this)[0].src+='?'
    })