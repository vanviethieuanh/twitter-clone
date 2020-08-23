module.exports = {
  transpileDependencies: ["vuetify"],
  chainWebpack: config => {
    config.plugin("html").tap(args => {
      args[0].title = "Twitter Clone";
      return args;
    });
  },

  outputDir: "./dist/",
  assetsDir: "./static/",
  indexPath: "./templates/index.html"
};
