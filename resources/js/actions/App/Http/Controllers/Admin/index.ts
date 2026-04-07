import DashboardController from './DashboardController'
import UserController from './UserController'
import ContentController from './ContentController'
const Admin = {
    DashboardController: Object.assign(DashboardController, DashboardController),
UserController: Object.assign(UserController, UserController),
ContentController: Object.assign(ContentController, ContentController),
}

export default Admin