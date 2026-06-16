const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: false
  },
  configureWebpack: {
    resolve: {
      fallback: {
        fs: false
      }
    }
  }
})
