import AuthForm from "./views/pages/AuthForm.js";
import LoanFeeForm from "./views/pages/CalculatorForm.js";

import Navbar from "./views/components/Navbar.js";

import Utils from "./services/Utils.js";

const routes = {
  "/": LoanFeeForm,
  "/login": AuthForm,
  "/logout": AuthForm,
  "/create-user": AuthForm
};

const app = async () => {
  const header = null || document.getElementById("header_container");
  const content = null || document.getElementById("page_container");

  header.innerHTML = await Navbar.render();
  await Navbar.after_render();

  // Get the parsed URl from the addressbar
  let request = Utils.parseRequestURL();

  // Parse the URL and if it has an id part, change it with the string ":id"
  let parsedURL =
    (request.resource ? "/" + request.resource : "/") +
    (request.id ? "/:id" : "") +
    (request.verb ? "/" + request.verb : "");

  // Get the page from our hash of supported routes.
  // If the parsed URL is not in our list of supported routes, select the 404 page instead
  let page = routes[parsedURL] ? routes[parsedURL] : Error404;
  content.innerHTML = await page.render();
  await page.after_render();
};

window.addEventListener("hashchange", app);

window.addEventListener("load", app);
