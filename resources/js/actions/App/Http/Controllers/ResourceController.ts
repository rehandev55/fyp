import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
const ResourceController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ResourceController.url(options),
    method: 'get',
})

ResourceController.definition = {
    methods: ["get","head"],
    url: '/resources',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
ResourceController.url = (options?: RouteQueryOptions) => {
    return ResourceController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
ResourceController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ResourceController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
ResourceController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: ResourceController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
    const ResourceControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: ResourceController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
        ResourceControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ResourceController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\ResourceController::__invoke
 * @see app/Http/Controllers/ResourceController.php:9
 * @route '/resources'
 */
        ResourceControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ResourceController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    ResourceController.form = ResourceControllerForm
export default ResourceController