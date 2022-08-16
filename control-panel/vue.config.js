const {
  defineConfig
} = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

module.exports = {
  devServer: {
    port: 8000,
    proxy: {
      "/api": {
        target: 'http://driver:8888',
      },
    }
  }
}
