
import * as THREE from "three";
//const THREE = require('three');
const textureLoader = new THREE.TextureLoader();

function loadTexture(path){
    const texture = textureLoader.load(path);
    texture.colorSpace = THREE.SRGBColorSpace;
    console.log(texture);
    texture.magFilter = THREE.NearestFilter;
    texture.minFilter = THREE.NearestFilter;
    return texture;
}
const textures = {
    dirt: loadTexture('textures/dirt.png'),
    grass: loadTexture('textures/grass.png'),
    grassSide: loadTexture('textures/grass_side.png'),
}
export const blocks = {
    empty: {
      id: 0,
      name:'empty',
      visible: false
    },
    grass: {
      id: 1,
      name: 'grass',
      color: 0x046b42,
      material:[
        new THREE.MeshLambertMaterial({map: textures.grassSide}),//right
        new THREE.MeshLambertMaterial({map: textures.grassSide}),//left
        new THREE.MeshLambertMaterial({map: textures.grass}),//top
        new THREE.MeshLambertMaterial({map: textures.dirt}),//bottom
        new THREE.MeshLambertMaterial({map: textures.grassSide}),//front
        new THREE.MeshLambertMaterial({map: textures.grassSide})//back
      ]
    },
    dirt: {
      id: 2,
      name: 'dirt',
      color: 0x807020,
      material: new THREE.MeshLambertMaterial({map: textures.dirt})
    },
  };