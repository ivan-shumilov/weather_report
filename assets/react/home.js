var React, ReactRouter
var Link = ReactRouter.Link
var axios
var moment
var jQuery

class Home extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      weather: ''
    }
  }

  componentDidMount () {
    this.getPage()
  }

  getPage () {
    axios.post('/api/v1/forecast-now')
      .then(response => {
        this.setState({ weather: response.data })
      })
  }

  render () {
    return (
      <div className='wrapper'>
        <main role='main' className='container pt-5'>
          <div className='row'>
            <div className='col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12 pt-5'>
               Сейчас в погода {this.state.weather} градусов.
            </div>
          </div>
        </main>
      </div>
    )
  }
}

Home()
