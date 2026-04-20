import ContentController from './ContentController'
import DashboardController from './DashboardController'
import UserController from './UserController'
const Admin = {
    ContentController: Object.assign(ContentController, ContentController),
DashboardController: Object.assign(DashboardController, DashboardController),
UserController: Object.assign(UserController, UserController),
}

export default Admin