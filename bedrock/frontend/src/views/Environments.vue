<template>
  <v-container fluid>
    <BreadCrumbs />
    <v-card>
      <v-card-title>
        <v-text-field
          v-model="search"
          prepend-inner-icon="mdi-magnify"
          label="Search"
          clearable
          hide-details
          class="pb-1"
        ></v-text-field>
        <v-spacer />
        <v-dialog v-if="isAuthenticated" v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn class="mx-2" depressed fab small v-on="on">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12">
                    <v-select
                      v-model="editedItem.category"
                      :items="environmentCategory"
                      label="Category*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12">
                    <v-textarea
                      v-model="editedItem.description"
                      label="Description"
                      rows="1"
                    ></v-textarea>
                  </v-col>
                </v-row>
              </v-container>
              <small>* indicates required field</small>
            </v-card-text>
            <v-card-actions>
              <v-spacer />
              <v-btn color="blue darken0-1" text @click="close">Cancel</v-btn>
              <v-btn color="blue darken0-1" text @click="save">Save</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-btn class="mx-2" depressed fab small @click="loadResources(true)">
          <v-icon dark>mdi-reload</v-icon>
        </v-btn>
        <v-switch class="mx-2" label="Small" v-model="dense"></v-switch>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="getResource(resourceType)"
        :search="search"
        :single-expand="singleExpand"
        :expanded.sync="expanded"
        :loading="isLoading"
        :loading-text="loadingText"
        :dense="dense"
        item-key="name"
        show-expand
        class="elevation-1"
      >
        <template v-slot:item.name="{ item }">
          {{ item.name }} ({{ getServer(item.name).length }})
        </template>
        <template v-slot:item.category="{ item }">
          <v-chip small label>{{ item.category }}</v-chip>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)">
            mdi-pencil
          </v-icon>
          <v-icon small class="mr-2" @click="deleteItem(item.id)">
            mdi-delete
          </v-icon>
        </template>
        <template v-slot:expanded-item="{ headers, item }">
          <td :colspan="headers.length">
            <ServerModal
              v-for="server in getServer(item.name)"
              :key="server.id"
              :server="server"
            >
            </ServerModal>
          </td>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
import { getStatusColor } from '../utils/common';

import {
  FETCH_RESOURCES,
  CREATE_RESOURCE,
  UPDATE_RESOURCE,
  DELETE_RESOURCE,
} from '../store/actions.type';
import BreadCrumbs from '../components/BreadCrumbs';
import ServerModal from '../components/ServerModal';

export default {
  name: 'Environments',
  components: {
    BreadCrumbs,
    ServerModal,
  },
  data: () => ({
    resourceType: 'environments',
    loadingText: 'Loading environments, please wait.',
    dense: false,
    dialog: false,
    expanded: [],
    singleExpand: true,
    search: '',
    headers: [
      { text: 'Name', align: 'start', value: 'name', width: '90%' },
      { text: 'Category', align: 'end', value: 'category', width: '10%' },
    ],
    environments: [],
    environmentCategory: ['DEV', 'BETA', 'STAGE', 'PROD'],
    editedIndex: -1,
    editedItem: {
      name: '',
      category: '',
      description: '',
    },
    defaultItem: {
      name: '',
      category: '',
      description: '',
    },
  }),
  created() {
    this.loadResources();
    if (this.isAuthenticated) {
      this.headers[0].width = '80%';
      this.headers.push({
        text: 'Actions',
        value: 'actions',
        align: 'end',
        sortable: false,
        width: '10%',
      });
    }
    this.headers.push({ text: '', value: 'data-table-expand' });
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? 'New Environment' : 'Edit Environment';
    },
    ...mapGetters({
      getResource: 'getResource',
      getResourceByField: 'getResourceByField',
      isLoading: 'isLoading',
      isAuthenticated: 'isAuthenticated',
    }),
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  methods: {
    loadResources(force = false) {
      if (this.getResource(this.resourceType).length === 0 || force) {
        this.fetchResources(this.resourceType);
      }
      if (this.getResource('servers').length === 0 || force) {
        this.fetchResources('servers');
      }
    },
    editItem(item) {
      this.editedIndex = this.getResource(this.resourceType).indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(id) {
      confirm('Are you sure you want to delete this item?') &&
        this.removeResource({ type: 'environments', id: id });
    },
    close() {
      this.dialog = false;
      setTimeout(() => {
        this.editedItem = Object.assign({}, this.defaultItem);
        this.editedIndex = -1;
      }, 300);
    },

    save() {
      if (this.editedIndex > -1) {
        this.updateResource({
          type: 'environments',
          resource: this.editedItem,
        });
      } else {
        this.createResource({
          type: 'environments',
          resource: this.editedItem,
        });
      }
      this.close();
    },

    getServer(environmentName) {
      return this.getResourceByField(
        'servers',
        'environments',
        environmentName
      );
    },

    getStatusColor: getStatusColor,

    ...mapActions({
      fetchResources: FETCH_RESOURCES,
      createResource: CREATE_RESOURCE,
      updateResource: UPDATE_RESOURCE,
      removeResource: DELETE_RESOURCE,
    }),
  },
};
</script>

<style></style>
