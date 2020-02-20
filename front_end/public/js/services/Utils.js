const Utils = {
  // --------------------------------
  //  Parse a url and break it into resource, id and verb
  // --------------------------------
  parseRequestURL: () => {
    let url = location.hash.slice(1).toLowerCase() || "/";
    let r = url.split("/");
    let request = {
      resource: null,
      id: null,
      verb: null
    };
    request.resource = r[1];
    request.id = r[2];
    request.verb = r[3];

    return request;
  },

  sleep: ms => {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
};

export const makeRequest = async (payload, url) => {
    const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
    };
    try {
        const response = await fetch(
          url,
          options
        );
        return response;
      } catch (err) {
        alert(err);
    }
};

export default Utils;

