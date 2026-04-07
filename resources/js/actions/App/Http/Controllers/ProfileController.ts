import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
/**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
const ProfileController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ProfileController.url(options),
    method: 'get',
})

ProfileController.definition = {
    methods: ["get","head"],
    url: '/profile',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
ProfileController.url = (options?: RouteQueryOptions) => {
    return ProfileController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
ProfileController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ProfileController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
ProfileController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: ProfileController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
    const ProfileControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: ProfileController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
        ProfileControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ProfileController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\ProfileController::__invoke
 * @see app/Http/Controllers/ProfileController.php:9
 * @route '/profile'
 */
        ProfileControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ProfileController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    ProfileController.form = ProfileControllerForm
export default ProfileController