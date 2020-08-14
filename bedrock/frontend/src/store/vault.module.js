import { VaultApiService } from '../services/api.service';
import mutation from './mutations.type';
import action from './actions.type';

const state = {
  items: [],
  logins: [],
  notes: [],
  loading: true,
  error: null,
};

const getters = {
  isLoading: state => state.loading,
  getVaultItems: state => state.items,
  getVaultLogins: state => state.logins,
  getVaultNotes: state => state.notes,
  getVault: state => [...state.items, ...state.logins, ...state.notes],
  getVaultByType: state => type => {
    return state[type];
  },
};

const mutations = {
  [mutation.FETCH_PENDING](state, status) {
    state.loading = status;
  },
  [mutation.SET_VAULT_RESOURCE](state, { type, resource }) {
    state[type] = resource;
  },
  [mutation.ADD_VAULT_RESOURCE](state, { type, resource }) {
    state[type].push(resource);
  },
  [mutation.EDIT_VAULT_RESOURCE](state, { type, updatedResource }) {
    const index = state[type].findIndex(
      resource => resource.id === updatedResource.id
    );
    Object.assign(state[type][index], updatedResource);
  },
  [mutation.REMOVE_VAULT_RESOURCE](state, { type, id }) {
    const index = state[type].findIndex(resource => resource.id === id);
    state[type].splice(index, 1);
  },
};

const actions = {
  [action.FETCH_VAULT_RESOURCE]({ commit }, type) {
    commit(mutation.FETCH_PENDING, true);
    return VaultApiService.get(type)
      .then(response => {
        commit(mutation.SET_VAULT_RESOURCE, {
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
  [action.CREATE_VAULT_RESOURCE]({ commit }, { type, resource }) {
    commit(mutation.FETCH_PENDING, true);
    return VaultApiService.post(type, resource)
      .then(response => {
        commit(mutation.ADD_VAULT_RESOURCE, {
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
  [action.UPDATE_VAULT_RESOURCE]({ commit }, { type, resource }) {
    commit(mutation.FETCH_PENDING, true);
    return VaultApiService.update(type, resource.id, resource)
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
  [action.DELETE_VAULT_RESOURCE]({ commit }, { type, id }) {
    commit(mutation.FETCH_PENDING, true);
    return VaultApiService.delete(`${type}/${id}`)
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
