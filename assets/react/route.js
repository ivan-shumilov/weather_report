var ReactRouter
var ReactDOM
var Router = ReactRouter.Router
var Route = ReactRouter.Route
var browserHistory = ReactRouter.browserHistory
var Home

ReactDOM.render(
  <Router history={browserHistory}>
    <Route path='/' component={Home} />
  </Router>,
  document.getElementById('app')
)
