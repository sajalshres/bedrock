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
        <Labels />
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
                <v-row dense>
                  <v-col cols="12" class="ma-0 pa-1">
                    <v-text-field
                      v-model="editedItem.name"
                      label="Name*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" class="ma-0 pa-1">
                    <v-text-field
                      v-model="editedItem.ip_address"
                      label="IP Address*"
                      required
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="6" class="ma-0 pa-1">
                    <v-select
                      v-model="editedItem.category"
                      :items="serverCategory"
                      label="Category*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" class="ma-0 pa-1">
                    <v-select
                      v-model="editedItem.operating_system"
                      :items="getOperatingSystemNames"
                      label="Operating System*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" class="ma-0 pa-1">
                    <v-select
                      v-model="editedItem.domain"
                      :items="getDomainNames"
                      label="Domains*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" class="ma-0 pa-1">
                    <v-select
                      v-model="editedItem.cluster"
                      :items="getClusterNames"
                      label="Cluster*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" class="ma-0 pa-1">
                    <v-autocomplete
                      v-model="editedItem.labels"
                      :items="getLabelNames"
                      label="Labels*"
                      chips
                      multiple
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" class="ma-0 pa-1">
                    <v-autocomplete
                      v-model="editedItem.environments"
                      :items="getEnvironmentNames"
                      label="Environments*"
                      chips
                      multiple
                    >
                    </v-autocomplete>
                  </v-col>
                  <v-col cols="12" sm="6" class="ma-0 pa-1">
                    <v-select
                      v-model="editedItem.owner"
                      :items="getOwnerNames"
                      label="Owner*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="6" class="ma-0 pa-1">
                    <v-select
                      v-model="editedItem.status"
                      :items="serverStatus"
                      label="Status*"
                      required
                    ></v-select>
                  </v-col>
                  <v-col cols="12" class="ma-0 pa-1">
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
        :headers="getHeaders"
        :items="getServers"
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
        <template v-slot:item.environments="{ item }">
          <v-chip
            label
            small
            class="ml-2 my-2"
            v-for="environment in item.environments"
            :key="environment"
            >{{ environment }}</v-chip
          >
        </template>
        <template v-slot:item.labels="{ item }">
          <v-chip
            label
            small
            class="ml-2 my-2"
            v-for="label in item.labels"
            :key="label"
            >{{ label }}</v-chip
          >
        </template>
        <template v-slot:item.status="{ item }">
          <v-chip
            small
            :x-small="dense"
            :color="getStatusColor(item.status)"
            dark
            >{{ item.status }}</v-chip
          >
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
          <td :colspan="headers.length">{{ item.description }}</td>
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
import Labels from '../components/Labels';

export default {
  name: 'Server',
  components: {
    BreadCrumbs,
    Labels,
  },
  data: () => ({
    resourceType: 'servers',
    resourceTypes: [
      'servers',
      'labels',
      'clusters',
      'environments',
      'domains',
      'owners',
      'operating_systems',
    ],
    loadingText: 'Loading Servers, Please wait.',
    dense: false,
    dialog: false,
    expanded: [],
    singleExpand: true,
    search: '',
    editedIndex: -1,
    editedItem: {
      name: '',
      ip_address: '',
      category: '',
      owner: '',
      domain: '',
      cluster: '',
      environments: [],
      operating_system: '',
      labels: [],
      status: '',
      description: '',
    },
    defaultItem: {
      name: '',
      ip_address: '',
      category: '',
      owner: '',
      domain: '',
      cluster: '',
      environments: [],
      operating_system: '',
      labels: [],
      status: '',
      description: '',
    },
    serverCategory: ['MAIL', 'FTP', 'PROXY', 'APP', 'BUILD'],
    serverStatus: ['ACTIVE', 'INACTIVE', 'DECOM'],
  }),
  created() {
    this.loadResources();
  },
  computed: {
    getHeaders() {
      const headers = [
        { text: 'Name', align: 'start', value: 'name' },
        { text: 'IP Address', value: 'ip_address', align: 'end' },
        { text: 'Owner', value: 'owner', align: 'end' },
        { text: 'Domain', value: 'domain', align: 'end' },
        { text: 'Cluster', value: 'cluster', align: 'end' },
        { text: 'Environments', value: 'environments', align: 'end' },
      ];

      if (this.$vuetify.breakpoint.name === 'xl') {
        headers.push({ text: 'Category', value: 'category', align: 'end' });
        headers.push({
          text: 'Operating System',
          value: 'operating_system',
          align: 'end',
        });
        headers.push({ text: 'Labels', value: 'labels', align: 'end' });
      }

      headers.push({ text: 'Status', value: 'status', align: 'end' });

      if (this.isAuthenticated) {
        headers.push({
          text: 'Actions',
          value: 'actions',
          align: 'end',
          sortable: false,
        });
      }
      headers.push({ text: '', value: 'data-table-expand' });

      return headers;
    },
    formTitle() {
      return this.editedIndex === -1 ? 'New Server' : 'Edit Server';
    },
    getEnvironmentNames() {
      return this.getEnvironments.map(({ name }) => name);
    },
    getClusterNames() {
      return this.getClusters.map(({ name }) => name);
    },
    getOwnerNames() {
      return this.getOwners.map(({ name }) => name);
    },
    getOperatingSystemNames() {
      return this.getOperatingSystems.map(({ name }) => name);
    },
    getDomainNames() {
      return this.getDomains.map(({ name }) => name);
    },
    getLabelNames() {
      return this.getLabels.map(({ name }) => name);
    },
    ...mapGetters([
      'isLoading',
      'isAuthenticated',
      'getResource',
      'getServers',
      'getEnvironments',
      'getClusters',
      'getOwners',
      'getOperatingSystems',
      'getDomains',
      'getLabels',
    ]),
  },
  watch: {
    dialog(val) {
      val || this.close();
    },
  },
  methods: {
    loadResources(force = false) {
      this.resourceTypes.forEach(resourceType => {
        if (this.getResource(resourceType).length === 0 || force) {
          this.fetchResources(resourceType);
        }
      });
    },

    editItem(item) {
      this.editedIndex = this.getResource(this.resourceType).indexOf(item);
      this.editedItem = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(id) {
      confirm('Are you sure you want to delete this item?') &&
        this.removeResource({ type: 'servers', id: id });
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
          type: 'servers',
          resource: this.editedItem,
        });
      } else {
        this.createResource({
          type: 'servers',
          resource: this.editedItem,
        });
      }
      this.close();
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
