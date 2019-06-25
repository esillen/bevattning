import React from 'react';

class RandomImage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
        error: null,
        isLoaded: false,
        randomImageUrl: null
    };
  }

  componentDidMount() {
    this.loadRandomImage();
  }

  loadRandomImage() {
    
    console.log("hejj");
    
    let api_key = "aFFKTuSMjd6j0wwjpFCPXZipQbcnw3vB";
    let q = "water";
    let limit = 1;
    let offset = Math.floor(Math.random() * 20);
    let rating = "g";
    let lang = "en";
    let fmt = "json";
    let url = `https://api.giphy.com/v1/gifs/search?api_key=${api_key}&q=${q}&limit=${limit}&offset=${offset}&rating=${rating}&lang=${lang}&fmt=${fmt}`;
    
    
    fetch(url)
      .then((result) => result.json())
      .then((json) => {
        console.log(json.data[0].images);
          this.setState({
            isLoaded: true,
            randomImageUrl: json.data[0].images.original.url
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error: error
          });
        }
      );
      

  }

  
  render() {
    const { error, isLoaded, randomImageUrl } = this.state;
    return (
      <div>
        <img src={randomImageUrl} />
      </div>
    );
  }
}


export default RandomImage;
