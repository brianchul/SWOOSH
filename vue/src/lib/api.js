import axios from 'axios';
import { config } from '../config';
const API_HOST = config.API_HOST;

export const request = ({
  baseURL = API_HOST,
  method = 'get',
  endpoint = '',
  params = {},
  data = {},
  formdata = null,
  uri = '',
  headers = {},
  auth = false,
}) => {
  if (auth) {
    const token = localStorage.getItem('accessToken');
    if (token) {
      headers.Authorization = `Bearer ${token}`;
      // fetchOptions.headers.AccessToken = token;
    } else {
      throw Error("No Token")
    }
  }

  if (formdata) {
    var bodyFormData = new FormData();
    bodyFormData.set("media",formdata.file)
    bodyFormData.set("articleID",formdata.articleID)
    data = bodyFormData
  }
  return axios({
    headers,
    ...(uri ? { url: uri } : { baseURL, url: endpoint }),
    ...(method.toUpperCase() === 'GET' ? { params } : { method, params, data }),
  })
};