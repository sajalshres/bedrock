import { SorApiService } from '../services/api.service';
import mutation from './mutations.type';
import action from './actions.type';

const state = {
  servers: [],
  environments: [],
  clusters: [],
  products: [],
  owners: [],
  labels: [],
  operating_systems: [],
  domains: [],
  loading: true,
  error: null,
};
const getters = {
  isLoading(state) {
    return state.loading;
  },
  getResource: state => type => {
    return state[type];
  },
  getResourceByField: state => (type, field, value) => {
    return state[type].filter(resource => {
      if (Array.isArray(resource[field])) {
        return resource[field].includes(value);
      }
      return resource[field] === value;
    });
  },
  getServers: state => state.servers,
  getEnvironments: state => state.environments,
  getClusters: state => state.clusters,
  getProducts: state => state.products,
  getOwners: state => state.owners,
  getOperatingSystems: state => state.operating_systems,
  getDomains: state => state.domains,
  getLabels: state => state.labels,
};

const mutations = {
  [mutation.FETCH_PENDING](state, status) {
    state.loading = status;
  },
  [mutation.SET_RESOURCES](state, { type, resources }) {
    state[type] = resources;
  },
  [mutation.ADD_RESOURCE](state, { type, resource }) {
    state[type].push(resource);
  },
  [mutation.EDIT_RESOURCE](state, { type, updatedResource }) {
    const index = state[type].findIndex(
      resource => resource.id === updatedResource.id
    );
    Object.assign(state[type][index], updatedResource);
  },
  [mutation.REMOVE_RESOURCE](state, { type, id }) {
    const index = state[type].findIndex(resource => resource.id === id);
    state[type].splice(index, 1);
  },
};

const actions = {
  [action.FETCH_RESOURCES]({ commit }, type) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.get(type)
      .then(response => {
        commit(mutation.SET_RESOURCES, {
          type: type,
          resources: response.data,
        });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
  [action.CREATE_RESOURCE]({ commit }, { type, resource }) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.post(type, resource)
      .then(response => {
        commit(mutation.ADD_RESOURCE, {
          type: type,
          resource: response.data,
        });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
  [action.UPDATE_RESOURCE]({ commit }, { type, resource }) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.update(type, resource.id, resource)
      .then(response => {
        commit(mutation.EDIT_RESOURCE, {
          type: type,
          updatedResource: response.data,
        });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
  [action.DELETE_RESOURCE]({ commit }, { type, id }) {
    commit(mutation.FETCH_PENDING, true);
    return SorApiService.delete(`${type}/${id}`)
      .then(response => {
        commit(mutation.FETCH_PENDING, false);
        commit(mutation.REMOVE_RESOURCE, { type: type, id: id });
      })
      .catch(error => {
        commit(mutation.SET_SNACKBAR, {
          message: error.message,
          color: 'error',
        });
      })
      .then(() => {
        commit(mutation.FETCH_PENDING, false);
      });
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
