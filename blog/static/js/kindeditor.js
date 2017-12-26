   KindEditor.ready(function(K) {
                window.editor = K.create('#id_content',{
                        width:"100%",
                        height:"500px",
                        resizeType:0,
                        uploadJson:"/uploadFile/",
                        extraFileUploadParams:{
                           csrfmiddlewaretoken:$("[name='csrfmiddlewaretoken']").val(),
                       }

                });

     })