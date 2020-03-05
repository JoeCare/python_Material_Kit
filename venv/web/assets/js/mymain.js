function getsighnup(){
    var data ={
                username: document.getElementById("userName").value,
                useremail: document.getElementById("userMail").value,
                password: document.getElementById("password").value,
                confirm_password: document.getElementById("confirm_password").value,}
    eel.createUser(data)

}

eel.expose(success_message);
function success_message(){
    toastr.options = {
                  "closeButton": true,
                  "debug": false,
                  "newestOnTop": true,
                  "progressBar": true,
                  "positionClass": "toast-top-right",
                  "preventDuplicates": true,
                  "onclick": null,
                  "showDuration": "300",
                  "hideDuration": "1000",
                  "timeOut": "5000",
                  "extendedTimeOut": "1000",
                  "showEasing": "swing",
                  "hideEasing": "linear",
                  "showMethod": "fadeIn",
                  "hideMethod": "fadeOut"
                }
     toastr["success"]("Data Inseted", "Success")
}