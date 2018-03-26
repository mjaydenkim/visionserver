import React from 'react';
import Dropzone from 'react-dropzone'
import axios from 'axios'

var instance = axios.create({
    baseURL: 'http://localhost:5000/image',
    timeout: 1000,
    headers: {'Access-Control-Allow-Origin': true},
    crossDomain: true
});

export default class ImgUploader extends React.Component{
    state = {imageString:""}
    
    readImage(acceptedFile){
	console.log('new image detecteddddddddddddddddd')

	acceptedFile.forEach(file => {
	    let imageReader = new FileReader();
	    imageReader.readAsDataURL( file );
	    imageReader.onload = (event) => {
		console.log(event.target.result);
		const b64image=event.target.result.split(',')[1];
		instance.post('/',{'image':b64image}).then(
		    function (response) {
			console.log(response.json());
		    }
		)
            };
            imageReader.onabort = () => console.log('file reading was aborted');
            imageReader.onerror = () => console.log('file reading has failed');
	    

	})
    }

    uploadFile(event) {
	let files = event.target.files || event.dataTransfer.files;
        if (!files.length) {
            console.log('no files');
        }
	const myFile = files[0];
	let data = new FormData();
	data.append('image', myFile, myFile.name);
	const config = {
            headers: { 'content-type': 'multipart/form-data' }
        }

        instance.post('/', data, config).then(function(response){
	    console.log(response);
	})
	
    }
    
    render(){
	return (
	    <div>
		<input type="file" onChange={this.uploadFile} />
	    </div>
	)
    }
}
//<!--	<Dropzone onDrop = {this.readImage}/> -->
