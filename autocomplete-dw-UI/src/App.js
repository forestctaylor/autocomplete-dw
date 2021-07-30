import './App.css';

function App() {

  function getSearchSuggestions(e) {
    const searchString = e.target.value;
    console.log(`Searching for ${searchString}`);

    var xhr = new XMLHttpRequest();
    xhr.onload = function (e) {
      console.log(xhr.status);
    };
    xhr.open('POST', 'http://localhost:5000/getSearchSuggestions');
    xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
    xhr.send(searchString); // TODO: JSON.stringify({searchString: searchString})
  }

  return (
    <div className="App">
      <header className="App-header">
        <form>
          <label className="App-label">
            Please search below!
          </label>
          <input className="App-input" type="text" name="search" onChange={getSearchSuggestions}/>
        </form>
        </header>
    </div>
  );
}

export default App;
