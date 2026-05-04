import ContentController from './ContentController'
import UserController from './UserController'
import DashboardController from './DashboardController'
const Admin = {
    ContentController: Object.assign(ContentController, ContentController),
UserController: Object.assign(UserController, UserController),
DashboardController: Object.assign(DashboardController, DashboardController),
}

export default Admin