import React from "react";

class UrlShortener extends React.Component {
  constructor(props) {
    super(props);
    this.API_URI = "/api/shorten/";

    this.state = {
      url: "",
      link: ""
    };

    this.updateTextState = this.updateTextState.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    fetch(this.API_URI, {
      method: "POST",
      headers: {
        "Content-Type": "application/json;charset=utf-8",
      },
      body: JSON.stringify(this.state),
    })
      .then((resp) => resp.json())
      .then((json) => this.setState({link: json.source_tag}));
  }

  updateTextState(event) {
    this.setState({ url: event.target.value });
  }

  render() {
    return (
      <div className="url-shortener">
        <h1>Url Shortener</h1>
        <form onSubmit={this.handleSubmit}>
          <label htmlFor="url">Url to shorten:</label>
          <input
            type="text"
            name="url"
            id="url"
            value={this.state.url}
            onChange={this.updateTextState}
            required
          />
          <button type="submit">Shorten!</button>
        </form>
        <div>Your shortened url is: /short/{this.state.link}</div>
      </div>
    );
  }
}

function App() {
  return <UrlShortener />;
}

export default App;
