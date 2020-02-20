import { makeRequest } from "../services/Utils.js";

export const CreateUser = async (payload) => {
  const url = `${process.env.API_URL}/auth/create`;
  let response = await makeRequest(payload, url);
  return response;
};

export const LoginUser = async (payload) => {
  const url = `${process.env.API_URL}/auth/login`;
  let response = await makeRequest(payload, url);
  return response;
};