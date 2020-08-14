// sor actions types
export const FETCH_RESOURCES = 'fetchResources';
export const FETCH_RESOURCE = 'fetchResource';
export const CREATE_RESOURCE = 'createResource';
export const UPDATE_RESOURCE = 'updateResource';
export const DELETE_RESOURCE = 'deleteResource';

// vault actions types
export const FETCH_VAULT_RESOURCE = 'fetchVaultResource';
export const CREATE_VAULT_RESOURCE = 'createVaultResource';
export const UPDATE_VAULT_RESOURCE = 'updateVaultResource';
export const DELETE_VAULT_RESOURCE = 'deleteVaultResource';

// auth action types
export const LOGIN = 'login';
export const LOGOUT = 'logout';
export const USER_UPDATE = 'updateUser';
export const CHECK_AUTH = 'checkAuth';
export const REFRESH_AUTH = 'refreshAuth';

export default {
  FETCH_RESOURCES,
  FETCH_RESOURCE,
  CREATE_RESOURCE,
  UPDATE_RESOURCE,
  DELETE_RESOURCE,
  FETCH_VAULT_RESOURCE,
  CREATE_VAULT_RESOURCE,
  UPDATE_VAULT_RESOURCE,
  DELETE_VAULT_RESOURCE,
  LOGIN,
  LOGOUT,
  USER_UPDATE,
  CHECK_AUTH,
  REFRESH_AUTH,
};
