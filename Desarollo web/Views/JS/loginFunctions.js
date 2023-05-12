let email_enterprise = "";
let password_enterprise = "";

function loginEnterprise(){
    email_enterprise = document.getElementById("email_enterprise").value;
    password_enterprise = document.getElementById("password_enterprise").value;
    if(email_enterprise == "" || password_enterprise == ""){
        alert("Please fill all the fields");
    }
    else{
        self.open('MainPageEnterprise.html', 'Ventana principal', 'width=300,height=200')
        
        // method that open another html
        /*let data = {
            email: email_enterprise,
            password: password_enterprise
        }
        fetch('http://localhost:3000/enterprise/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(res => res.json())
        .then(data => {
            if(data.status == 200){
                localStorage.setItem("token", data.token);
                localStorage.setItem("email", data.email);
                localStorage.setItem("name", data.name);
                localStorage.setItem("role", data.role);
                window.location.href = "http://localhost:3000/enterprise";
            }
            else{
                alert(data.message);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });*/
    }
} 