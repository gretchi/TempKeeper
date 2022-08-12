<template>
  <div class="row">
    <div class="col col-parent">
      <p class="el bg-black">{{ locationName }}</p>
    </div>

    <!-- Arrow down -->
    <div class="col-1 col-parent">
      <button
        v-on:click="
          presetTemp -= 0.5;
          setNode();
        "
        class="button el"
      >
        <i class="bi bi-caret-down-fill"></i>
      </button>
    </div>

    <!-- presetTemp -->
    <div class="col col-parent">
      <p
        class="el bg-blue"
        :class="{
          'bg-blue': autoCtrl,
          'bg-black': !autoCtrl,
        }"
      >
        {{ presetTemp.toFixed(1) }}℃
      </p>
    </div>

    <!-- Arrow up -->
    <div class="col-1 col-parent">
      <button
        v-on:click="
          presetTemp += 0.5;
          setNode();
        "
        class="button el"
      >
        <i class="bi bi-caret-up-fill"></i>
      </button>
    </div>

    <div class="col col-parent">
      <div v-if="autoCtrl">
        <div v-if="plugStatus">
          <p class="el bg-red">運転中</p>
        </div>
        <div v-else>
          <p class="el bg-gray">停止中</p>
        </div>
      </div>
      <div v-else>
        <p class="el bg-gray">手動停止</p>
      </div>
    </div>

    <!-- 自動停止ボタン -->
    <div class="col-2 col-parent">
      <button
        v-on:click="
          autoCtrl = 0;
          setNode();
        "
        class="button el"
        :class="{
          'bg-gray': autoCtrl,
          'bg-yellow': !autoCtrl,
        }"
      >
        停止
      </button>
    </div>

    <!-- 自動ボタン -->
    <div class="col-2 col-parent">
      <button
        v-on:click="
          autoCtrl = 1;
          setNode();
        "
        class="button el"
        :class="{
          'bg-green': autoCtrl,
          'bg-gray': !autoCtrl,
        }"
      >
        自動
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    nodeId: Number,
  },
  data: function () {
    return {
      locationName: "",
      presetTemp: 20.0,
      autoCtrl: 0,
      plugStatus: 0,
    };
  },
  methods: {
    getNode: function () {
      axios.get("/api/node/" + this.nodeId).then((res) => {
        const data = res.data;
        this.locationName = data.location_name;
        this.presetTemp = data.preset_temp;
        this.plugStatus = data.status;
        this.autoCtrl = data.auto_control;
      });
    },
    setNode: function () {
      axios
        .post("/api/node/" + this.nodeId, {
          auto_control: this.autoCtrl,
          preset_temp: this.presetTemp,
        })
        .then((res) => {
          const data = res.data;
          this.locationName = data.location_name;
          this.plugStatus = data.status;
          this.autoCtrl = data.auto_control;
        });
    },
  },
  mounted: function () {
    this.getNode();
    setInterval(() => {
      this.getNode();
    }, 15000);
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
