// common mutation types
export const FETCH_PENDING = 'fetchPending';
export const RESET_STATE = 'resetModuleState';
export const SET_ERROR = 'setError';

// sor mutation types
export const SET_RESOURCES = 'setResources';
export const SET_RESOURCE = 'setResource';
export const ADD_RESOURCE = 'addResource';
export const EDIT_RESOURCE = 'editResource';
export const REMOVE_RESOURCE = 'removeResource';

// vault mutation types
export const SET_VAULT_RESOURCE = 'setVaultResource';
export const ADD_VAULT_RESOURCE = 'addVaultResource';
export const EDIT_VAULT_RESOURCE = 'editVaultResource';
export const REMOVE_VAULT_RESOURCE = 'removeVaultResource';

// snack bar mutation types
export const SET_SNACKBAR = 'setSnackBar';

// auth mutation types
export const SET_AUTH = 'setUser';
export const PURGE_AUTH = 'logOut';

export default {
  FETCH_PENDING,
  RESET_STATE,
  SET_ERROR,
  SET_RESOURCES,
  SET_RESOURCE,
  ADD_RESOURCE,
  EDIT_RESOURCE,
  REMOVE_RESOURCE,
  SET_VAULT_RESOURCE,
  ADD_VAULT_RESOURCE,
  EDIT_VAULT_RESOURCE,
  REMOVE_VAULT_RESOURCE,
  SET_SNACKBAR,
  SET_AUTH,
  PURGE_AUTH,
};
