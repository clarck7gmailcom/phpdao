import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
/** @type import('hardhat/config').HardhatUserConfig */
const config: HardhatUserConfig = {
  solidity: {
    version: "0.8.18",
    settings: {
      optimizer: {
        enabled: true,
        runs: 1000,
      },
    },
},
  networks: {
    Sepolia: {
      url: `https://sepolia.infura.io/v3/e5887c2141934ba7adbc485fdcb1c08a`,
      accounts: ["578836bc21ad3da291d8befab06448930f239d15ac2b8c6a5b7b96a966ce4942"]
    }
  }
};
export default config;
