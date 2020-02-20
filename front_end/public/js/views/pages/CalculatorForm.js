import CalculateFee from "../../actions/calculator.js";
import Utils from "../../services/Utils.js";

let LoanFeeForm = {
  render: async () => {
    return /*html*/ `
            <section>
                <div>
                    <span id="login-message"> Please Login to perform this operation </span>
                </div>
                <div class="row">
                    <div class="col-25">
                      <label>Loan Amount</label>
                    </div>
                    <div class="col-75">
                      <input class="input" id="amount" type="number" min="1000" max="20000" onchange="if(this.value>20000){this.value='20000';}else if(this.value<1000){this.value='1000';}" placeholder="Enter loan amount" />
                    </div>
                </div>
                <div class="row">
                    <div class="col-25">
                      <label>Tenure</label>
                    </div>
                    <div class="col-75">
                      <select class="input" id="tenure">
                        <option value=12>12</option>
                        <option value=24>24</option>
                      </select>
                    </div>
                </div>
                <div class="row">
                    <div class="col-25">
                      <label>Loan Fee:</label>
                    </div>
                    <div class="col-75">
                      <label id="loan-fee"></label>
                    </div>
                </div>
                <div class="field">
                    <p class="control">
                        <button class="btn btn-primary" id="submit_btn">
                          <div class="calculate-button" id="loader-submit">Submit</div>
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
    let token = window.localStorage.getItem("token")

    if (token === null) {
        document.getElementById("login-message").style.display = "block";
        document.getElementById("submit_btn").disabled = true;
    } else {
        document.getElementById("login-message").style.display = "none";
        document.getElementById("submit_btn").disabled = false;
    }

    document
      .getElementById("submit_btn")
      .addEventListener("click", async () => {
        let amount = document.getElementById("amount");
        let tenure = document.getElementById("tenure");
        if (
          (amount.value == "") |
          (tenure.value == "")
        ) {
          alert(`The fields cannot be empty`);
        } else {
          const payload = {
            loan_amount: amount.value,
            tenure: tenure.value
          };

          document.getElementById("loader-submit").classList.add("loader");
          document.getElementById("loader-submit").innerHTML = "";

          try {
            let response = await CalculateFee(payload, token);
            if (response.status === 200){
                const data = await response.json();
                document.getElementById("loan-fee").innerHTML = "£"+ data.loan_fee;
            } else {
                alert(`Calculation Failed`);
            }
            document
              .getElementById("loader-submit")
              .classList.remove("loader");
            document.getElementById("loader-submit").innerHTML = "Submit";
          } catch (err) {
            document
              .getElementById("loader-submit")
              .classList.remove("loader");
            document.getElementById("loader-submit").innerHTML = "Submit";
            let x = document.getElementById("snackbar");
            x.innerHTML = "Error calculating fee";
            x.className = "show";
            setTimeout(function() {
              x.className = x.className.replace("show", "");
            }, 3000);
          }
        }
      });
  }
};

export default LoanFeeForm;
