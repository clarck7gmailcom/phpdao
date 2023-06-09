// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;
import "./Merklelibrary.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HID is ERC721, ERC721URIStorage, Ownable {
    string _name = "HID";
    string _symbol = "HID";
    // Counters.Counter默认为0
    using Counters for Counters.Counter;
    // using Address for address;

    Counters.Counter private _tokenIdCounter;
    mapping(address => bool) isMinted;
    // 测试ERC6551时先注释掉
    bytes32 root;

    constructor() ERC721(_name, _symbol) {}

    // 用户调用铸币函数
    // 测试ERC6551时先注释掉
    // function mint(address to, bytes32[] memory proof) external {
        function mint(address to) external {
        // bool canMint = isMember(proof, to);
        // require(canMint, "You are not the Member");
        // require(!isMinted[to], "You've already mint it");
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
        // _mint(to, tokenId);
        isMinted[to] = true;
    }

    function isMember(bytes32[] memory proof, address UserAddress)
        private
        view
        returns (bool)
    {
        bytes32 leaf = keccak256(abi.encodePacked(UserAddress));
        return MerkleProof.verify(proof, root, leaf);
    }

    function changeRoot(bytes32 newRoot) external onlyOwner {
        root = newRoot;
    }

    // 注销HID
    function _burn(uint256 tokenId)
        internal
        override(ERC721, ERC721URIStorage)
    {
        require(
            msg.sender == ERC721.ownerOf(tokenId),
            "Only the HID owner can call this function"
        );
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    // 查看是否支持接口
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) external {
        require(
            msg.sender == ERC721.ownerOf(tokenId),
            "Only the HID owner can call this function"
        );
        require(
            _exists(tokenId),
            "ERC721URIStorage: URI set of nonexistent token"
        );
        _setTokenURI(tokenId, _tokenURI);
    }

    // 重写方法，不用erc721的功能
    function approve(address to, uint256 tokenId)
        public
        override(ERC721, IERC721)
    {}

    // 重写方法，不用erc721的功能
    function setApprovalForAll(address operator, bool approved)
        public
        override(ERC721, IERC721)
    {}

    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public override(IERC721, ERC721) {}

    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes memory data
    ) public override(IERC721, ERC721) {}
}
