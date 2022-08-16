<template>
  <div class="container">
    <PanelHeader title="主ヒータ運転操作パネル" />
    <HeaterControlRow v-for="node in nodes" :key="node.id" :nodeId="node.id" />
    <BlankRow />
    <BlankRow />
    <BlankRow />
    <PanelFooter />
  </div>
</template>

<script>
import axios from "axios";

import PanelHeader from "@/components/PanelHeader.vue";
import HeaterControlRow from "@/components/HeaterControlRow.vue";
import BlankRow from "@/components/BlankRow.vue";
import PanelFooter from "@/components/PanelFooter.vue";

export default {
  components: {
    PanelHeader,
    HeaterControlRow,
    BlankRow,
    PanelFooter,
  },
  data: function () {
    return {
      nodes: [],
    };
  },
  methods: {
    getNodes: function () {
      axios.get("/api/nodes").then((res) => {
        const data = res.data;
        this.nodes = data.filter((node) => node.plug_mac);
      });
    },
  },
  mounted: function () {
    this.getNodes();
  },
};
</script>

<style>
#app {
  margin-top: 90px;
}
</style>
