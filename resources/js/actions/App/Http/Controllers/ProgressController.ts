import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
const ProgressController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ProgressController.url(options),
    method: 'get',
})

ProgressController.definition = {
    methods: ["get","head"],
    url: '/progress',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
ProgressController.url = (options?: RouteQueryOptions) => {
    return ProgressController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
ProgressController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: ProgressController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
ProgressController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: ProgressController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
    const ProgressControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: ProgressController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
        ProgressControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ProgressController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\ProgressController::__invoke
 * @see app/Http/Controllers/ProgressController.php:9
 * @route '/progress'
 */
        ProgressControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: ProgressController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    ProgressController.form = ProgressControllerForm
export default ProgressController