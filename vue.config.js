const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    https: true
  },
  configureWebpack: {
    resolve: {
      fallback: {
        fs: false
      }
    }
  }
})
