<template>
  <div class="row">
    <div class="col col-parent">
      <a :href="getSelfHostUrl('/')">
        <button class="button el bg-magenta">メイン<br />メニュ</button>
      </a>
    </div>
    <div class="col col-parent">
      <a :href="getSelfHostUrl('/configure/')">
        <button class="button el bg-yellow">ノード管理</button>
      </a>
    </div>

    <div class="col col-parent">
      <a :href="getSelfHostUrl('/', 5050)">
        <button class="button el bg-yellow">DB管理</button>
      </a>
    </div>

    <div class="col col-parent">
      <a :href="getSelfHostUrl('/', 3000)">
        <button class="button el bg-yellow">ダッシュ<br />ボード</button>
      </a>
    </div>

    <div class="col col-parent"></div>

    <div class="col col-parent">
      <button class="button el bg-green">疎通正常</button>
    </div>
    <div class="col col-parent">
      <button class="button el bg-green">温度正常</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {},
  data: function () {
    return {};
  },
  methods: {
    getSelfHostUrl: function (path, port = null) {
      const host = window.location.host;
      const hostname = window.location.hostname;
      const protocol = window.location.protocol;

      if (window.location.port === "8000" && path !== "/") {
        return protocol + "//" + hostname + ":8080" + path;
      }

      if (port !== null) {
        return protocol + "//" + hostname + ":" + port + path;
      }

      return protocol + "//" + host + path;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
