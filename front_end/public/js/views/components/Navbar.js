let Navbar = {
  render: async () => {
    let view = /*html*/ `
            <nav class="navbar">
              <div class="container">
                <h1 class="heading-logo"><a href="#/">Fee Calculator</a></h1>
                <ul id="nav-actions" class="nav nav-right">
                </ul>
              </div>
          </nav>
        `;
    return view;
  },
  after_render: async () => {
    const loginActions = `
          <li><a href="#/">Home</a></li>
          <li><a href="#/login">Login</a></li>
          <li><a href="#/create-user">Sign up</a></li>
    `;

    const logoutActions = `
          <li><a href="#/">Home</a></li>
          <li><a href="#/logout">Logout</a></li>
    `;
    let token = window.localStorage.getItem("token");

    if (token === null) {
        document.getElementById("nav-actions").innerHTML = loginActions;
    } else {
        document.getElementById("nav-actions").innerHTML = logoutActions;
    }
  }
};

export default Navbar;