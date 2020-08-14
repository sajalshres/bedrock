import axios from 'axios';
import JwtService from './jwt.service';
import store from '../store';
import { PURGE_AUTH } from '../store/mutations.type';
import { REFRESH_AUTH } from '../store/actions.type';

const ApiClient = axios.create({
  baseURL: '/api',
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
  },
  timeout: 10000,
});

ApiClient.interceptors.response.use(
  response => {
    return response;
  },
  error => {
    if (error.response.status !== 401) {
      return new Promise((resolve, reject) => {
        reject(error);
      });
    }

    console.log({ error });
    if (error.config.url === 'auth/token/refresh/') {
      store.commit(PURGE_AUTH);

      return new Promise((resolve, reject) => {
        reject(error);
      });
    }

    if (error.response.data.code === 'token_not_valid') {
      return Promise.all([store.dispatch(REFRESH_AUTH)])
        .then(() => {
          const config = error.config;
          config.headers['Authorization'] = `Bearer ${JwtService.getToken()}`;
          ApiClient.defaults.headers.common[
            'Authorization'
          ] = `Bearer ${JwtService.getToken()}`;

          return new Promise((resolve, reject) => {
            axios
              .request(config)
              .then(response => {
                console.log(response);
                resolve(response);
              })
              .catch(error => {
                reject(error);
              });
          });
        })
        .catch(error => {
          Promise.reject(error);
        });
    }
  }
);

const ApiService = {
  setHeader() {
    ApiClient.defaults.headers.common[
      'Authorization'
    ] = `Bearer ${JwtService.getToken()}`;
  },
  get(resource, slug = '') {
    return ApiClient.get(`${resource}/${slug}`, {});
  },
  post(resource, params) {
    return ApiClient.post(`${resource}`, params);
  },
  update(resource, slug, params) {
    return ApiClient.put(`${resource}/${slug}`, params);
  },
  put(resource, params) {
    return ApiClient.put(`${resource}`, params);
  },
  delete(resource) {
    return ApiClient.delete(`${resource}`);
  },
};

export default ApiService;

export const SorApiService = {
  get(resource, slug = '') {
    return ApiService.get(`sor/${resource}`, slug);
  },
  post(resource, params) {
    return ApiService.post(`sor/${resource}/`, params);
  },
  update(resource, slug, params) {
    return ApiService.put(`sor/${resource}/${slug}/`, params);
  },
  put(resource, params) {
    return ApiService.put(`sor/${resource}/`, params);
  },
  delete(resource) {
    return ApiService.delete(`sor/${resource}/`);
  },
};

export const VaultApiService = {
  get(resource, slug = '') {
    return ApiService.get(`vault/${resource}`, slug);
  },
  post(resource, params) {
    return ApiService.post(`vault/${resource}/`, params);
  },
  update(resource, slug, params) {
    return ApiService.put(`vault/${resource}/${slug}/`, params);
  },
  put(resource, params) {
    return ApiService.put(`vault/${resource}/`, params);
  },
  delete(resource) {
    return ApiService.delete(`vault/${resource}/`);
  },
};
