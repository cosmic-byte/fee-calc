import * as Auth from "../../actions/auth.js";
import Utils from "../../services/Utils.js";

let AuthForm = {
  render: async () => {
    return /*html*/ `
            <section>
              <h2 id="title" class="page-title">Auth</h2>
                <div class="row">
                    <div class="col-25">
                      <label>Email</label>
                    </div>
                    <div class="col-75">
                      <input class="input" id="email" type="text" placeholder="Enter your email" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-25">
                      <label>Password</label>
                    </div>
                    <div class="col-75">
                      <input class="input" id="password" type="password" placeholder="Enter your password" />
                    </div>
                </div>
                <div class="field">
                    <p class="control">
                        <button class="btn btn-primary" id="submit_btn">
                          <div class="" id="loader-login">Submit</div>
                        </button>
                    </p>
                </div>

                <div id="snackbar"></div>

            </section>
        `;
  },
  // All the code related to DOM interactions and controls go in here.
  // This is a separate call as these can be registered only after the DOM has been painted
  after_render: async () => {
    let request = Utils.parseRequestURL();

    if (request.resource === "logout"){
        window.localStorage.removeItem("token");
        window.location.href = "#/login";
    } else {
        let pageTitle = document.getElementById("title");
        request.resource === "create-user" ? pageTitle.innerHTML = "Create User" : pageTitle.innerHTML = "Login";

        document
          .getElementById("submit_btn")
          .addEventListener("click", async () => {
            let email = document.getElementById("email");
            let password = document.getElementById("password");
            if (
              (email.value == "") |
              (password.value == "")
            ) {
              alert(`The fields cannot be empty`);
            } else {
              const payload = {
                email: email.value,
                password: password.value
              };

              document.getElementById("loader-login").classList.add("loader");
              document.getElementById("loader-login").innerHTML = "";

              try {
                let response =
                  request.resource === "create-user"
                    ? await Auth.CreateUser(payload)
                    : await Auth.LoginUser(payload);
                if (response.status === 200 || response.status === 201){
                    const data = await response.json();
                    window.localStorage.setItem("token", data.token);
                    window.location.href = "#/";
                } else {
                    document
                      .getElementById("loader-login")
                      .classList.remove("loader");
                    document.getElementById("loader-login").innerHTML = "Submit";
                    alert(`Authentication Failed`);
                }

              } catch (err) {
                document
                  .getElementById("loader-login")
                  .classList.remove("loader");
                document.getElementById("loader-login").innerHTML = "Submit";
                let x = document.getElementById("snackbar");
                x.innerHTML = "Error posting auth data";
                x.className = "show";
                setTimeout(function() {
                  x.className = x.className.replace("show", "");
                }, 3000);
              }
            }
          });
    }
  }
};

export default AuthForm;
