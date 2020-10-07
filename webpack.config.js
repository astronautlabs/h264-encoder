/* eslint-disable @typescript-eslint/no-var-requires */
const path = require("path");

const createConfig = (target, libraryTarget) => ({
  devtool: "source-map",
  entry: "./h264-encoder.ts",
  module: {
    rules: [
      {
        loader: "ts-loader",
        test: /\.ts$/u
      }
    ]
  },
  node: {
    fs: "empty"
  },
  output: {
    filename: 'h264-encoder.' + target + '.js',
    path: path.join(__dirname, "embuild/dist"),
    library: "HME",
    libraryTarget
  },
  target,
  resolve: {
    extensions: [
      ".ts",
      ".js"
    ]
  }
})

module.exports = [
  createConfig("node", "commonjs2"),
  createConfig("web", "var"),
];
