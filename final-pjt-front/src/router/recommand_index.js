import RecoMainView from '@/views/reco_vue/RecoMainView'
import ResultRecoView from '@/views/reco_vue/ResultRecoView'


export default [
    {
      path: '/recomain',
      name: 'recomaintview',
      component: RecoMainView
    },
    {
      path: '/recores',
      name: 'resultrecoview',
      component: ResultRecoView
      
    },
]