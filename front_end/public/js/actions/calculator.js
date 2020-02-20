
let CalculateFee = async (payload, token) => {
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + token
    },
    body: JSON.stringify(payload)
  };
  try {
    const response = await fetch(
      `${process.env.API_URL}/core/calculate-fee`,
      options
    );
    const rs = await response;
    return rs;
  } catch (err) {
    alert(err);
  }
};


export default CalculateFee;

