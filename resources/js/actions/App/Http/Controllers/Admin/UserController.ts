import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../../wayfinder'
/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
const UserController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: UserController.url(options),
    method: 'get',
})

UserController.definition = {
    methods: ["get","head"],
    url: '/admin/users',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
UserController.url = (options?: RouteQueryOptions) => {
    return UserController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
UserController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: UserController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
UserController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: UserController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
    const UserControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: UserController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
        UserControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: UserController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\Admin\UserController::__invoke
 * @see app/Http/Controllers/Admin/UserController.php:10
 * @route '/admin/users'
 */
        UserControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: UserController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    UserController.form = UserControllerForm
export default UserController