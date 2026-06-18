import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
import { queryParams, type RouteQueryOptions, type RouteDefinition, type RouteFormDefinition } from './../../../../wayfinder'
/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
const PracticeController = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: PracticeController.url(options),
    method: 'get',
})

PracticeController.definition = {
    methods: ["get","head"],
    url: '/practice',
} satisfies RouteDefinition<["get","head"]>

/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
PracticeController.url = (options?: RouteQueryOptions) => {
    return PracticeController.definition.url + queryParams(options)
}

/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
PracticeController.get = (options?: RouteQueryOptions): RouteDefinition<'get'> => ({
    url: PracticeController.url(options),
    method: 'get',
})
/**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
PracticeController.head = (options?: RouteQueryOptions): RouteDefinition<'head'> => ({
    url: PracticeController.url(options),
    method: 'head',
})

    /**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
    const PracticeControllerForm = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
        action: PracticeController.url(options),
        method: 'get',
    })

            /**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
        PracticeControllerForm.get = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: PracticeController.url(options),
            method: 'get',
        })
            /**
* @see \App\Http\Controllers\PracticeController::__invoke
 * @see app/Http/Controllers/PracticeController.php:9
 * @route '/practice'
 */
        PracticeControllerForm.head = (options?: RouteQueryOptions): RouteFormDefinition<'get'> => ({
            action: PracticeController.url({
                        [options?.mergeQuery ? 'mergeQuery' : 'query']: {
                            _method: 'HEAD',
                            ...(options?.query ?? options?.mergeQuery ?? {}),
                        }
                    }),
            method: 'get',
        })
    
    PracticeController.form = PracticeControllerForm
export default PracticeController