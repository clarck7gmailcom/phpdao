pragma solidity ^0.8.18;

import "@openzeppelin/contracts/utils/Create2.sol";
import "./../interfaces/IERC6551Registry.sol";

/**
 * SampleRegistry Contract
 */
contract SampleAccountRegistry is IERC6551Registry {
    error InitializationFailed();
// createAccount- 在给定地址的情况下为 ERC-721 令牌部署令牌绑定帐户implementation
/**
每个代币绑定账户的部署字节码应具有以下结构：
ERC-1167 Header               (10 bytes)
<implementation (address)>    (20 bytes)
ERC-1167 Footer               (15 bytes)
<salt (uint256)>              (32 bytes)
<chainId (uint256)>           (32 bytes)
<tokenContract (address)>     (32 bytes)
<tokenId (uint256)>           (32 bytes)
*/
    function createAccount(
        address implementation,
        uint256 chainId,
        address tokenContract,
        uint256 tokenId,
        uint256 salt,
        bytes calldata initData
    ) external returns (address) {
        bytes memory code = _creationCode(implementation, chainId, tokenContract, tokenId, salt);

        address _account = Create2.computeAddress(
            bytes32(salt),
            keccak256(code)
        );

        if (_account.code.length != 0) return _account;

        _account = Create2.deploy(0, bytes32(salt), code);

        if (initData.length != 0) {
            (bool success, ) = _account.call(initData);
            if (!success) revert InitializationFailed();
        }

        emit AccountCreated(
            _account,
            implementation,
            chainId,
            tokenContract,
            tokenId,
            salt
        );

        return _account;
    }
// account- 一个只读函数，用于计算给定地址的 ERC-721 令牌的令牌绑定帐户地址implementation
    function account(
        address implementation,
        uint256 chainId,
        address tokenContract,
        uint256 tokenId,
        uint256 salt
    ) external view returns (address) {
        bytes32 bytecodeHash = keccak256(
            _creationCode(implementation, chainId, tokenContract, tokenId, salt)
        );

        return Create2.computeAddress(bytes32(salt), bytecodeHash);
    }

    function _creationCode(
        address implementation_,
        uint256 chainId_,
        address tokenContract_,
        uint256 tokenId_,
        uint256 salt_
    ) internal pure returns (bytes memory) {
        return
            abi.encodePacked(
                hex"3d60ad80600a3d3981f3363d3d373d3d3d363d73",
                implementation_,
                hex"5af43d82803e903d91602b57fd5bf3",
                abi.encode(salt_, chainId_, tokenContract_, tokenId_)
            );
    }
}